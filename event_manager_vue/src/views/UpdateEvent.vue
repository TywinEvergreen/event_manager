<template>
    <EventCreateUpdateCard v-if="event.detailed_event.creator.id === user.user.id">
        <v-row>
            <v-col cols="6">
                <v-text-field
                        type="text"
                        v-model="form.title"
                        label="Название события"
                        outlined
                        counter="50"
                        :error-messages="title_errors"
                />
            </v-col>
            <v-col cols="6">
                <v-combobox
                        type="text"
                        v-model="form.type"
                        :items="types.slice(0, 5)"
                        outlined
                        label="Тип события"
                        counter="20"
                        :error-messages="type_errors"
                ></v-combobox>
            </v-col>
            <v-col cols="12">
                <v-text-field
                        type="text"
                        v-model="form.spending_date_time"
                        class="mt"
                        outlined
                        label="Дата проведения"
                        :error-messages="spending_date_time_errors"
                ></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-textarea
                        type="text"
                        v-model="form.text"
                        class="mt"
                        outlined
                        label="Описание события"
                        :error-messages="text_errors"
                ></v-textarea>
            </v-col>
            <v-col cols="12" justify="end">
                <v-row justify="end">
                    <v-btn
                            style="margin-top: -20px; left: -10px"
                            color="primary"
                            @click="update_event"
                    >
                        Обновить событие
                    </v-btn>
                </v-row>
            </v-col>
        </v-row>
    </EventCreateUpdateCard>
    <ErrorMessage v-else error="403" text="У вас нет доступа к этой странице"/>
</template>

<script>
    import EventCreateUpdateCard from "../components/cards/EventCreateUpdateCard"
    import ErrorMessage from "../components/ErrorMessage"
    import Axios from 'axios'
    import qs from 'qs'
    import {validationMixin} from 'vuelidate'
    import {required, maxLength} from 'vuelidate/lib/validators'
    import {mapState, mapActions} from 'vuex'

    export default {
        name: "UpdateEvent",
        mixins: [validationMixin],
        components: {
            EventCreateUpdateCard,
            ErrorMessage
        },
        data() {
            return {
                types: [],
                form: {
                    title: '',
                    type: '',
                    text: '',
                    spending_date_time: '',
                },
                validation: {
                    title: {
                        errors: [],
                        has_error: false,
                    },
                    type: {
                        errors: [],
                        has_error: false
                    },
                    text: {
                        errors: [],
                        has_error: false
                    },
                    spending_date_time: {
                        errors: [],
                        has_error: false
                    },
                }
            }
        },
        validations: {
            form: {
                title: {
                    required,
                    titleMaxLength: maxLength(50)
                },
                type: {
                    required,
                    maxLength: maxLength(20)
                },
                text: {
                    required
                },
                spending_date_time: {
                    required
                }
            }
        },
        mounted() {
            this.set_detailed_event(this.$route.params.slug)
                .then(response => {
                    this.form.title = this.event.detailed_event.title;
                    this.form.type = this.event.detailed_event.type.title;
                    this.form.text = this.event.detailed_event.text;
                    this.form.spending_date_time = this.event.detailed_event.spending_date_time;
                })
        },
        computed: {
            ...mapState(['event', 'user']),
            title_errors() {
                const errors = [];
                if (this.$v.form.title.$dirty) {
                    !this.$v.form.title.required && errors.push('This field may not be blank.');
                    !this.$v.form.title.titleMaxLength && errors.push('Max length of this field is 50.');
                }
                this.validation.title.errors.forEach(error => {
                    errors.push(error);
                });
                return errors;
            },
            type_errors() {
                const errors = [];
                if (this.$v.form.type.$dirty) {
                    !this.$v.form.type.required && errors.push('This field may not be blank.');
                    !this.$v.form.type.maxLength && errors.push('Max length of this field is 20.');
                }
                this.validation.type.errors.forEach(error => {
                    errors.push(error);
                });
                return errors;
            },
            text_errors() {
                const errors = [];
                if (this.$v.form.text.$dirty) {
                    !this.$v.form.text.required && errors.push('This field may not be blank.');
                }
                this.validation.text.errors.forEach(error => {
                    errors.push(error);
                });
                return errors;
            },
            spending_date_time_errors() {
                const errors = [];
                if (this.$v.form.spending_date_time.$dirty) {
                    !this.$v.form.spending_date_time.required && errors.push('This field may not be blank.');
                }
                this.validation.spending_date_time.errors.forEach(error => {
                    errors.push(error);
                });
                return errors;
            },
        },
        methods: {
            ...mapActions(['set_detailed_event']),
            update_event() {
                this.$v.$touch();
                if (!this.$v.form.$anyError) {
                    Axios('events/' + this.$route.params.slug, {
                        method: 'PATCH',
                        data: qs.stringify({
                            title: this.form.title,
                            type: this.form.type,
                            text: this.form.text,
                            spending_date_time: this.form.spending_date_time
                        })
                    })
                        .then(response => {
                            this.$router.push({name: 'event_detail', params: {slug: this.$route.params.slug}})
                        })
                        .catch(error => {
                            Object.entries(error.response.data).forEach(error => {
                                this.validation[error[0]].errors.push(error[1][0]);
                                this.validation[error[0]].has_error = true;
                            });
                            this.$v.$touch();
                        });
                }
            }
        }
    }
</script>

<style scoped>
    .mt {
        margin-top: -25px;
    }
</style>

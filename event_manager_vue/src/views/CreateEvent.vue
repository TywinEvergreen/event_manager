<template>
    <EventCreateUpdateCard>
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
                        type="datetime-local"
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
                            @click="create_event"
                    >
                        Создать событие
                    </v-btn>
                </v-row>
            </v-col>
        </v-row>
    </EventCreateUpdateCard>
</template>

<script>
    import EventCreateUpdateCard from "../components/cards/EventCreateUpdateCard";
    import Axios from 'axios'
    import qs from 'qs'
    import {validationMixin} from 'vuelidate';
    import {required, maxLength} from 'vuelidate/lib/validators'

    export default {
        name: "CreateEvent",
        mixins: [validationMixin],
        components: {
            EventCreateUpdateCard
        },
        data() {
            return {
                types: [],
                form: {
                    title: '',
                    type: '',
                    text: '',
                    spending_date_time: ''
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
        computed: {
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
        mounted() {
            this.get_types()
        },
        methods: {
            get_types() {
                if (this.types.length === 0) {
                    Axios.get('events/types/').then(response => {
                        response.data.results.map(type => {
                            this.types.push(type.title)
                        })
                    })
                }
            },
            create_event() {
                this.$v.$touch();
                if (!this.$v.form.$anyError) {
                    Axios('events/', {
                        method: 'POST',
                        data: qs.stringify({
                            title: this.form.title,
                            type: this.form.type,
                            text: this.form.text,
                            spending_date_time: this.form.spending_date_time
                        })
                    })
                        .then(response => {
                            this.$router.push({name: 'event_list'});
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

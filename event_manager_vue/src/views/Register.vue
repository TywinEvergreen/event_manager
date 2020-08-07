<template>
    <AuthCard>
        <v-row justify="center">
            <v-col cols="12">
                <v-text-field
                        v-model="form.username"
                        label="Имя пользователя"
                        outlined
                        :error-messages="username_errors"
                        @input="reset_main_form('username')"
                ></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-text-field
                        type='email'
                        label="E-mail"
                        outlined
                        style="margin-top: -20px"
                        v-model="form.email"
                        :error-messages="email_errors"
                        @input="reset_main_form('email')"
                />
            </v-col>
            <v-col cols="12">
                <v-text-field
                        type='password'
                        label="Пароль"
                        outlined
                        style="margin-top: -20px"
                        v-model="form.password"
                        :error-messages="password_errors"
                        @input="reset_password_form"
                />
            </v-col>
            <v-col cols="12">
                <v-text-field
                        type='password'
                        label="Подтверждение пароля"
                        outlined
                        style="margin-top: -20px"
                        v-model="form.confirm_password"
                        :error-messages="confirm_password_errors"
                        @input="$v.form.confirm_password.$reset()"
                />
            </v-col>
            <v-row align="center" justify="end">
                <v-btn
                        style="margin-top: -10px; left: -22px"
                        color="primary"
                        @click="register"
                >
                    Регистрация
                </v-btn>
            </v-row>
        </v-row>
    </AuthCard>
</template>

<script>
    import AuthCard from '../components/cards/AuthCard'
    import Axios from 'axios';
    import qs from 'qs';
    import {mapActions} from 'vuex';
    import {validationMixin} from 'vuelidate';
    import {required, sameAs} from 'vuelidate/lib/validators';

    export default {
        name: "Register",
        mixins: [validationMixin],
        components: {
            AuthCard
        },
        data() {
            return {
                form: {
                    username: '',
                    email: '',
                    password: '',
                    confirm_password: '',
                },
                validation: {
                    username: {
                        has_error: false,
                        errors: []
                    },
                    email: {
                        has_error: false,
                        errors: []
                    },
                    password: {
                        has_error: false,
                        errors: []
                    }
                }
            };
        },
        validations: {
            form: {
                username: {required},
                password: {required},
                email: {required},
                confirm_password: { // Пофиксить confirm_password
                    required,
                    sameAsPassword: sameAs('password')
                },
            }
        },
        computed: {
            username_errors() {
                const errors = [];
                if (this.$v.form.username.$dirty) {
                    !this.$v.form.username.required && errors.push('This field may not be blank.');
                }
                this.validation.username.errors.forEach(error => {
                    errors.push(error);
                });
                return errors;
            },
            email_errors() {
                const errors = [];
                if (this.$v.form.email.$dirty) {
                    !this.$v.form.email.required && errors.push('This field may not be blank.');
                }
                this.validation.email.errors.forEach(error => {
                    errors.push(error);
                });
                return errors;
            },
            password_errors() {
                const errors = [];
                if (this.$v.form.password.$dirty) {
                    !this.$v.form.password.required && errors.push('This field may not be blank.');
                }
                this.validation.password.errors.forEach(error => {
                    errors.push(error);
                });
                return errors;
            },
            confirm_password_errors() {
                const errors = [];
                if (this.$v.form.confirm_password.$dirty) {
                    !this.$v.form.confirm_password.required && errors.push('This field may not be blank.');
                    !this.$v.form.confirm_password.sameAsPassword && errors.push('Passwords must match.');
                }
                return errors;
            },
        },
        methods: {
            ...mapActions(['LOGIN']),
            reset_password_form() {
                this.validation.password.errors = [];
                this.validation.password.has_error = false;
            },
            reset_main_form(form) {
                this.validation[form].errors = [];
                this.validation[form].has_error = false;
            },
            register() {
                this.$v.$touch();
                if (!this.$v.form.$anyError) {
                    Axios('auth/users/', {
                        method: 'POST',
                        data: qs.stringify({
                            username: this.form.username,
                            email: this.form.email,
                            password: this.form.password,
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
    };
</script>

<style scoped>
</style>
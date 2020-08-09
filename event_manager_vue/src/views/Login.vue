<template>
    <AuthCard>
        <v-row justify="center">
            <v-col cols="12">
                <v-text-field
                        type="text"
                        label="Имя пользователя"
                        outlined
                        v-model="form.username"
                        :error-messages="login_errors"
                        @input="reset_form"
                        @keydown.enter="login(form)"
                />
            </v-col>
            <v-col cols="12">
                <v-text-field
                        type='password'
                        label="Пароль"
                        outlined
                        style="margin-top: -20px"
                        v-model="form.password"
                        :error-messages="login_errors"
                        @input="reset_form"
                        @keydown.enter="login(form)"
                />
            </v-col>
            <v-col cols="12">
                <v-row justify="end">
                    <v-btn
                            style="margin-top: -20px; left: -10px"
                            color="primary"
                            @click="login(form)"
                    >
                        Войти
                    </v-btn>
                </v-row>
            </v-col>
        </v-row>
    </AuthCard>
</template>

<script>
    import AuthCard from "../components/cards/AuthCard";
    import Axios from "axios";
    import qs from 'qs';
    import Cookies from 'js-cookie';
    import {validationMixin} from 'vuelidate';
    import {mapActions} from 'vuex'

    export default {
        name: "Login",
        components: {
            AuthCard
        },
        mixins: [validationMixin],
        data() {
            return {
                form: {
                    username: null,
                    password: null,
                },
                unable_to_login: false,
                errors: []
            };
        },
        validations: {
            form: {username: {}, password: {}}
        },
        computed: {
            login_errors() {
                const errors = [];
                if (!this.$v.form.username.$dirty) return errors;
                this.errors.forEach(error => {
                    !this.$v.unable_to_login && errors.push(error);
                });
                return errors;
            },
        },
        methods: {
            ...mapActions(['set_authorization_header', 'set_user']),
            reset_form() {
                this.errors = [];
                this.unable_to_login = false;
            },
            login() {
                Axios('auth/token/login/', {
                    method: 'POST',
                    data: qs.stringify({
                        username: this.form.username,
                        password: this.form.password,
                    })
                })
                    .then(response => {
                        Cookies.set('auth_token', response.data.auth_token);
                        this.set_authorization_header();
                        this.set_user();
                        this.$router.push({name: 'event_list'})
                    })
                    .catch(error => {
                        Object.entries(error.response.data).forEach(error => {
                            this.errors.push(error[1][0]);
                            this.unable_to_login = true;
                            this.$v.$touch();
                        });
                    });
            }
        }
    };
</script>

<style scoped>
</style>

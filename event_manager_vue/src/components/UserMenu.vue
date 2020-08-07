<template>
    <div>
        <v-btn @click="show" icon>
            <v-icon>fas fa-user</v-icon>
        </v-btn>
        <v-menu
                v-model="show_user_menu"
                :position-x="x"
                :position-y="y"
                offset-y
        >
            <v-list>
                <v-list-item @click="goCreateEvent">
                    <v-list-item-title>Создать событие</v-list-item-title>
                </v-list-item>
                <v-list-item @click="sign_out">
                    <v-list-item-title>Выйти</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </div>
</template>

<script>
    import Cookies from 'js-cookie'
    import {mapState, mapActions} from 'vuex'

    export default {
        name: "UserMenu",
        data() {
            return {
                show_user_menu: false,
                x: 0,
                y: 48
            }
        },
        computed: {
            ...mapState(['user'])
        },
        methods: {
            ...mapActions(['set_authorization_header', 'set_user']),
            show(e) {
                e.preventDefault();
                this.show_user_menu = false;
                this.x = e.clientX;
                this.$nextTick(() => {
                    this.show_user_menu = true
                })
            },
            goCreateEvent() {
                this.$router.push({name: 'create_event'})
            },
            sign_out() {
                Cookies.remove('auth_token');
                this.set_authorization_header();
                this.set_user();
            },
        },
    }
</script>

<style scoped>
    .v-menu__content {
        position: absolute;
        background-color: white;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }
</style>

<template>
    <div>
        <v-app-bar dense dark>
            <v-toolbar-title class="clickable" @click="goEventList">Event Manager</v-toolbar-title>

            <v-spacer></v-spacer>

            <div v-if="user.show_authentication_menu">
                <UserMenu v-if="user.authenticated"/>

                <div v-else>
                    <MobileAuthorizationMenu class="d-flex d-sm-none"/>
                    <div class="hidden-xs-only">
                        <v-btn small class="green darken-3 ma-1" @click="goLogin">Вход</v-btn>
                        <v-btn small class="blue darken-3 ma-1" @click="goRegister">Регистрация</v-btn>
                    </div>
                </div>
            </div>

        </v-app-bar>
        <slot></slot>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import MobileAuthorizationMenu from './MobileAuthorizationMenu'
    import UserMenu from './UserMenu'

    export default {
        name: "Header",
        computed: {
            ...mapState(['user'])
        },
        components: {
            MobileAuthorizationMenu,
            UserMenu
        },
        methods: {
            goEventList() {
                this.$router.push({name: 'event_list'})
            },
            goLogin() {
                this.$router.push({name: 'login'})
            },
            goRegister() {
                this.$router.push({name: 'register'})
            },
        }
    }
</script>

<style scoped>
</style>

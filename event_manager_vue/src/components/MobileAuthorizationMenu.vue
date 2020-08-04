<template>
    <div>
        <v-btn @click="show" icon>
            <v-icon>fas fa-bars</v-icon>
        </v-btn>
        <v-menu
                v-model="show_authorization_menu"
                :position-x="x"
                :position-y="y"
                offset-y
        >
            <v-list>
                <v-list-item @click="goLogin">
                    <v-list-item-title>Вход</v-list-item-title>
                </v-list-item>
                <v-list-item @click="goRegister">
                    <v-list-item-title>Регистрация</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </div>
</template>

<script>
    export default {
        name: "AuthorizationMenu",
        data() {
            return {
                show_authorization_menu: false,
                x: 0,
                y: 48
            }
        },
        methods: {
            show(e) {
                e.preventDefault();
                this.show_authorization_menu = false;
                this.x = e.clientX;
                this.$nextTick(() => {
                    this.show_authorization_menu = true
                })
            },
            goLogin() {
                this.$router.push({name: 'login'})
            },
            goRegister() {
                this.$router.push({name: 'register'})
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

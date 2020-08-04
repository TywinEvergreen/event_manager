<template>
    <v-container>
        <v-row justify="center">
            <v-card
                    class="pa-5 ma-8"
                    style="max-width: 400px"
                    elevation="24"
            >
                <slot></slot>
            </v-card>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "AuthCard"
    }
</script>

<style scoped>

</style>
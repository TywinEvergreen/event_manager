<template>
    <v-row justify="center">
        <v-card
                class="pa-5 ma-8"
                style="max-width: 600px"
                elevation="24"
        >
            <slot></slot>
        </v-card>
    </v-row>
</template>

<script>
    export default {
        name: "EventCreateUpdateCard"
    }
</script>

<style scoped>

</style>
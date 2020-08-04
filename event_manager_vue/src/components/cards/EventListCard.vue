<template>
    <v-container>
        <v-row justify="center">
            <v-card
                    class="pa-5 ma-8"
                    style="width: 1200px"
                    elevation="24"
            >
                <slot></slot>
            </v-card>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "EventListCard"
    }
</script>

<style scoped>
</style>

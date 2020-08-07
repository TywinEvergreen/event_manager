<template>
    <v-container>
        <v-row class="mt-10" justify="center" align="center">
            <p>{{error}}</p>
            <v-divider class="mx-4 my-2" vertical/>
            <p>{{text}}</p>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "NotFound",
        props: ['error', 'text']
    }
</script>

<style scoped>
    p {
        margin-top: 10px
    }
</style>

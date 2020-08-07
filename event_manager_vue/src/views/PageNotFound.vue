<template>
    <ErrorMessage error="404" text="Страница не найдена"/>
</template>

<script>
    import ErrorMessage from "../components/ErrorMessage"
    export default {
        name: "PageNotFound",
        components: {
            ErrorMessage
        }
    }
</script>

<style scoped>
    p {
        margin-top: 10px
    }
</style>

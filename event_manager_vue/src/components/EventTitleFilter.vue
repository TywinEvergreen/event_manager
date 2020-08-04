<template>
    <v-text-field
            v-model="title_filter"
            filled
            label="Поиск по названию..."
            @keydown.enter="set_filter"
    />
</template>

<script>
    import {mapActions, mapState} from 'vuex'

    export default {
        name: "EventTitleFilter",
        data() {
            return {
                title_filter: ''
            }
        },
        methods: {
            ...mapActions(['set_title_filter', 'set_page', 'set_events']),
            set_filter() {
                this.set_page(1);
                this.set_title_filter(this.title_filter);
                this.set_events()
            }
        }
    }
</script>

<style scoped>

</style>
<template>
    <v-pagination
            v-if="total_pages > 1"
            @input="select_page"
            :value="event.page"
            :length="total_pages"
    ></v-pagination>
</template>

<script>
    import {mapState, mapGetters, mapActions} from 'vuex'

    export default {
        name: "EventPagination",
        computed: {
            ...mapState(['event']),
            ...mapGetters(['total_pages'])
        },
        methods: {
            ...mapActions(['set_page', 'set_events']),
            select_page(p) {
                this.set_page(p);
                this.set_events()
            },
        }
    }
</script>

<style scoped>

</style>
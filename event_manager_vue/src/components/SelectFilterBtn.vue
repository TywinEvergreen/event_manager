<template>
    <v-overflow-btn
            v-model="date_filter"
            :items="date_filter_types"
            filled
            label="Фильтр"
    ></v-overflow-btn>
</template>

<script>
    import {mapActions} from 'vuex'

    export default {
        name: "SelectFilterBtn",
        data() {
            return {
                date_filter: 'За последний месяц',
                date_filter_types: [
                    {text: 'За последний месяц'},
                    {text: 'За последнюю неделю'},
                    {text: 'За сегодня'},
                    {text: 'Все'},
                ]
            }
        },
        watch: {
            date_filter(NewDate_filter) {
                let dict = {
                    'За последний месяц': 'month',
                    'За последнюю неделю': 'week',
                    'За сегодня': 'day',
                    'Все': 'all'
                };
                this.set_page(1);
                this.set_date_filter(dict[NewDate_filter]);
                this.set_events()
            }
        },
        methods: {
            ...mapActions(['set_page', 'set_date_filter', 'set_events'])
        }
    }
</script>

<style scoped>

</style>
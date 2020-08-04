<template>
    <EventListCard>
        <v-row class="px-12 py-6">
            <v-row class="px-3 mb-6">
                <v-col cols="12" sm="6">
                    <h1>{{event.detailed_event.title}}</h1>
                </v-col>
                <v-col cols="12" sm="6">
                    <v-row justify="end" class="mt-2 d-none d-sm-flex">
                        <nobr class="caption">
                            <h3>Дата проведения</h3>
                            <h3>{{event.detailed_event.spending_date_time}}</h3>
                        </nobr>
                    </v-row>
                    <v-row class="ml-0 mt-n6 mb-4 d-flex d-sm-none">
                        <nobr class="caption">
                            Дата проведения
                            {{event.detailed_event.spending_date_time}}
                        </nobr>
                    </v-row>
                </v-col>
                <v-col cols="12" class="mt-n3 overline">
                    <nobr>
                        <h2>Тип события: {{event.detailed_event.type.title}}</h2>
                        <h2 class="mt-4">Автор: {{event.detailed_event.creator.username}}</h2>
                    </nobr>
                </v-col>
            </v-row>
            <v-col cols="12" class="mt-n6-4">
                <p>{{event.detailed_event.text}}</p>
            </v-col>
        </v-row>
    </EventListCard>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import EventListCard from "../components/cards/EventListCard";

    export default {
        name: "DetailEvent",
        components: {
            EventListCard
        },
        created() {
            this.set_detailed_event(this.$route.params.slug)
        },
        computed: {
            ...mapState(['event'])
        },
        methods: {
            ...mapActions(['set_detailed_event'])
        }
    }
</script>

<style scoped>

</style>

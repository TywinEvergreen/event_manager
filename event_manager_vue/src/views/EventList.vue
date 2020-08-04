<template>
    <v-container>
        <v-row class="mx-5" justify="end">
            <v-col cols="12" md="8">
                <EventTitleFilter/>
            </v-col>
            <v-col cols="12" md="4">
                <SelectFilterBtn/>
            </v-col>
        </v-row>

        <EventsNotFound v-if="event.nothing_loaded"/>
        <EventListCard class="mt-n12">
            <v-row v-if="!event.events_loading">
                <v-col cols="12" md="6" lg="4" v-for="e in event.events.results">
                    <EventCard :event="e"/>
                </v-col>
            </v-row>
            <v-row v-else>
                <v-col cols="12" md="6" lg="4" v-for="i in new Array(9)">
                    <ContentLoader height="170"/>
                </v-col>
            </v-row>
        </EventListCard>
        <v-row justify="end" class="mr-6">
            <div>
                <EventPagination/>
            </div>
        </v-row>
    </v-container>
</template>

<script>
    import Vue from 'vue'
    import SelectFilterBtn from "../components/SelectFilterBtn"
    import EventListCard from "../components/cards/EventListCard"
    import EventCard from "../components/cards/EventCard"
    import EventPagination from "../components/EventPagination"
    import EventTitleFilter from "../components/EventTitleFilter"
    import EventsNotFound from "../components/EventsNotFound"
    import {mapState, mapActions} from 'vuex'
    import {ContentLoader} from 'vue-content-loader'

    import lineClamp from 'vue-line-clamp';

    Vue.use(lineClamp);

    export default {
        name: "EventList",
        components: {
            SelectFilterBtn,
            EventListCard,
            EventCard,
            EventPagination,
            EventTitleFilter,
            EventsNotFound,
            ContentLoader
        },
        created() {
            this.set_events();
        },
        computed: {
            ...mapState(['event'])
        },
        methods: {
            ...mapActions(['set_events'])
        },
    }
</script>

<style scoped>
</style>

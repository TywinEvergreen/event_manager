<template>
    <v-card
            class="ma-auto px-7 pb-5"
            style="height: 150px; text-overflow: ellipsis; overflow: hidden"
            outlined
    >
        <v-row class="px-3 overline">
            <v-col cols="12" sm="6">
                <v-row>
                    {{event.date_time_created}}
                </v-row>
            </v-col>
            <v-col cols="12" sm="6">
                <v-row justify="end" class="d-none d-sm-flex">
                    {{event.spending_date_time}}
                </v-row>
                <v-row class="d-flex d-sm-none">
                    {{event.spending_date_time}}
                </v-row>
            </v-col>
        </v-row>
        <p class="headline mb-1 clickable" @click="goDetailEvent(event.slug)">
            {{event.title}}
        </p>
        <p v-line-clamp="3" class="overline">
            {{event.text}}
        </p>
    </v-card>
</template>

<script>
    export default {
        name: "EventCard",
        props: ['event'],
        methods: {
            goDetailEvent(slug) {
                this.$router.push({name: 'event_detail', params: {slug: slug}})
            }
        }
    }
</script>

<style scoped>

</style>

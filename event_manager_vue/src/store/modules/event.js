import Axios from "axios";
import Cookies from 'js-cookie';

const state = {
    events: [],
    detailed_event: {},
    title_filter: '',
    date_filter: 'month',
    page: 1,

    events_loading: false,
    nothing_loaded: undefined,
};

const getters = {
    date_filter: (state) => {
        return state.date_filter
    },
    total_pages: (state) => {
        return Math.ceil(state.events.count / 9);
    }
};

const mutations = {
    events: (state, payload) => {
        state.events = payload;
    },
    detailed_event: (state, payload) => {
        state.detailed_event = payload
    },
    title_filter: (state, payload) => {
        state.title_filter = payload
    },
    date_filter: (state, payload) => {
        state.date_filter = payload
    },
    page: (state, payload) => {
        state.page = payload
    },
    events_loading: (state, payload) => {
        state.events_loading = payload
    },
    nothing_loaded: (state, payload) => {
        state.nothing_loaded = payload
    },
};

const actions = {
    set_events: async ({commit, state}) => {
        commit('events_loading', true)
        Axios.get('events/', {
            params: {
                title_filter: state.title_filter,
                date_filter: state.date_filter,
                page: state.page
            }
        })
            .then(response => {
                if (response.data.results.length > 0) {
                    commit('events', response.data);
                    commit('events_loading', false)
                    commit('nothing_loaded', false)
                } else {
                    commit('events', [])
                    commit('nothing_loaded', true)
                }
            });
    },
    set_detailed_event: async ({commit}, slug) => {
        Axios.get('events/' + slug)
            .then(response => {
                commit('detailed_event', response.data)
            })
    },
    set_title_filter: async ({commit}, payload) => {
        commit('title_filter', payload)
    },
    set_date_filter: async ({commit}, payload) => {
        commit('date_filter', payload)
    },
    set_page: async ({commit, dispatch}, payload) => {
        commit('page', payload);
    }
};

export default {
    state,
    getters,
    mutations,
    actions
};

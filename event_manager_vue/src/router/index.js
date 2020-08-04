import Vue from 'vue'
import VueRouter from 'vue-router'
import EventList from '../views/EventList.vue'
import EventDetail from '../views/EventDetail.vue'
import Login from '../views/Login'
import Register from '../views/Register'
import CreateEvent from '../views/CreateEvent'
import PageNotFound from '../views/PageNotFound'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'event_list',
        component: EventList
    },
    {
        path: '/detail/:slug',
        name: 'event_detail',
        component: EventDetail
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/create_event',
        name: 'create_event',
        component: CreateEvent
    },
    {
        path: '*',
        name: 'page_not_found',
        component: PageNotFound
    },
];

const router = new VueRouter({
    history: true,
    routes: routes
});

export default router

import Vue from 'vue';
import VueRouter from 'vue-router';
import Feed from '../views/Feed.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Feed',
    component: Feed,
  },
  // {
  //   path: '/about',
  //   name: 'About',
  // },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;

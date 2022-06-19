import Vue from 'vue';
import Router from 'vue-router';
import Create from '@/components/Create';
import Books from '@/components/Books';
import BookDetail from '@/components/BookDetail';
import BookEdit from '@/components/BookEdit';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/create',
      name: 'create',
      component: Create,
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: BookDetail,
      props: true,
    },
    {
      path: '/edit/:id',
      name: 'edit',
      component: BookEdit,
      props: true,
    },
  ],
  mode: 'history',
});

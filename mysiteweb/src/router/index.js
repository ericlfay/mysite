import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/main/index'
import Login from '@/user/login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})

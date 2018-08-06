import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/main/index'
import Blog from '@/main/blog'

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
      path: '/blog',
      name: 'Blog',
      component: Blog
    }
  ]
})

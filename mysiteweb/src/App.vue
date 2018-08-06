<template>
  <div id="app">
   <header>
  <div class="tophead">
    <div class="logo"><a href="/">学习与成长</a></div>

    <nav class="topnav" id="topnav">
      <ul>
        <li v-for="item in items" :key="item.key">
        <router-link :to="{name: item.nav_url}">{{ item.nav_text }} </router-link>
          </li>
      </ul>
    </nav>
  </div>
</header>
    <router-view/>
  </div>
</template>

<script>
import {apiMenuList} from './api/api'

export default {
  name: 'App',
  data () {
    return {
      items: []
    }
  },
  created () {
    apiMenuList(this.ParamsData)
      .then((response) => {
        console.log(response)
        this.items = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>

<style>
  @import "./assets/css/base.css";
  @import "./assets/css/index.css";
  @import "./assets/css/m.css";
    .el-pager > .number {
    padding: 0px;
    background:none;
  }
</style>

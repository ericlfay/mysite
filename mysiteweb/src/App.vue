<template>
  <div id="app">
   <header>
  <div class="tophead">
    <div class="logo"><a href="/">学习与成长</a></div>

    <nav class="topnav" id="topnav">
      <ul>
        <li v-for="item in items" :key="item.key">
            <a href="index.html">{{ item.nav_text }}</a>
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
</style>

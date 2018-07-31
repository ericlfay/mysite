<template>
<article>
  <div class="blogs">
    <li v-for="item in items" :key="item.key">
      <span class="blogpic"><a href="/"><img :src="blog_pic_path + item.image"></a></span>
      <h3 class="blogtitle"><a href="/">{{item.title}}</a></h3>
      <div class="bloginfo">
        <p>{{item.excerpt}}</p>
      </div>
      <div class="autor"><span class="lm"><a href="/"  target="_blank" class="classname">{{item.category}}|{{item.tags}}</a></span><span class="dtime">{{item.created_time}}</span><span class="viewnum">浏览（<a href="/">{{item.views}}</a>）</span><span class="readmore"><a href="/">阅读原文</a></span></div>
    </li>
  </div>
  </article>
</template>

<script>
import {host, apiBlogList} from '../api/api'
export default {
  name: 'Index',
  data () {
    return {
      items: [],
      blog_pic_path: host + '/media/'
    }
  },
  created () {
    apiBlogList(this.ParamsData)
      .then((response) => {
        console.log(response)
        this.items = response.data.results
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>

<style scoped>

</style>

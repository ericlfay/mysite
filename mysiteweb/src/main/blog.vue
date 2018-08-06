<template>
<article>
   <div class="infos">
    <div class="newsview">
      <h3 class="news_title">{{Blog.title}}</h3>
      <div class="news_author">
      <span class="au01">{{Blog.author}}</span>
      <span class="au02">{{Blog.created_time}}</span>
      <span class="au03">共<b>{{Blog.views}}</b>人围观</span></div>
      <div class="tags"><a v-for="item in Blog.tags" :key="item" :label="item" :value="item">{{item}} &nbsp;</a></div>
      <div class="news_infos" v-html="compiledMarkdown">  </div>
    </div>
  </div>
  </article>
</template>

<script>
import {apiBlogInfo} from '../api/api'
import marked from 'marked'
var rendererMD = new marked.Renderer()
marked.setOptions({
  renderer: rendererMD,
  gfm: true,
  tables: true,
  breaks: false,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false
})

export default {
  name: 'Blog',
  data () {
    return {
      blog_id: this.$route.query.blog_id,
      Blog: ''
    }
  },
  created () {
    this.getBlog()
  },
  methods: {
    getBlog () {
      apiBlogInfo(this.blog_id)
        .then((response) => {
          console.log(response)
          this.Blog = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  computed: {
    compiledMarkdown: function () {
      return marked(this.Blog.contents, { sanitize: true })
    }
  }
}
</script>

<style scoped>
</style>

<template>
<article>
  <div class="blogs">
    <li v-for="item in items" :key="item.key">
      <span class="blogpic"><a href="/"><img :src="blog_pic_path + item.image"></a></span>
      <h3 class="blogtitle"><a href="/">{{item.title}}</a></h3>
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
        this.items = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>

<style scoped>

</style>

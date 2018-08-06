<template>
<article>
  <div class="blogs">
    <li v-for="item in items" :key="item.key">
      <span class="blogpic"><router-link :to="{ name: 'Blog', query: { blog_id: item.id }}"><img :src="blog_pic_path + item.image"></router-link></span>
      <h3 class="blogtitle"><router-link :to="{ name: 'Blog', query: { blog_id: item.id }}">{{item.title}}</router-link></h3>
      <div class="bloginfo">
        <p>{{item.excerpt}}</p>
      </div>
      <div class="autor">
      <span class="lm">
        <a href="/"  target="_blank" class="classname">{{item.category}}</a>|<a>{{item.tags}}</a>
      </span>
      <span class="dtime">{{item.created_time}}</span>
      <span class="viewnum">浏览（<a href="/">{{item.views}}</a>）</span>
        <span class="readmore"><router-link :to="{ name: 'Blog', query: { blog_id: item.id }}">阅读原文</router-link></span>
      </div>
    </li>
        <div class="pagelist nopadden">
    <el-pagination
      @size-change="handlePageSizeChange"
      @current-change="handlePageCurrentChange"
      :current-page="ParamsData.page"
      :page-sizes="[1, 5, 10, 20]"
      :page-size="ParamsData.size"
      layout="sizes, total, prev, pager, next, jumper"
      :total="Blog.count">
    </el-pagination>
  </div>
  </div>

  <div class="sidebar">
     <div class="search">
      <form  name="searchform" id="searchform" @keyup="searchClick" onSubmit="return false;">
        <input name="search" id="search" class="input_text" placeholder="请输入关键字" v-model="ParamsData.search" style="color: rgb(153, 153, 153);" type="text">
        <input name="Submit" class="input_submit" type="button" @click="searchClick" value="搜索">
      </form>
  </div>
          <div class="cloud">
      <h2 class="hometitle">标签</h2>
      <ul>
       <a v-for="item in tags" :key="item.name" :label="item" :value="item.id" @click="tagSearch(item.id)">{{item.name}} &nbsp;</a>
      </ul>
    </div>
    </div>

  </article>
</template>

<script>
import {host, apiBlogList, apiTagList} from '../api/api'
export default {
  name: 'Index',
  data () {
    return {
      ParamsData: {
        page: 1,
        size: 10,
        search: '',
        tag_id: ''
      },
      tags: '',
      items: [],
      blog_pic_path: host + '/media/'
    }
  },
  created () {
    this.getBlogList()
    this.getTagList()
  },
  methods: {
    handlePageSizeChange (val) {
      this.ParamsData.size = val
      this.getBlogList()
    },
    handlePageCurrentChange (val) {
      this.ParamsData.page = val
      this.getBlogList()
    },
    getBlogList () {
      apiBlogList(this.ParamsData)
        .then((response) => {
          this.items = response.data.results
          this.Blog = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getTagList () {
      apiTagList()
        .then((response) => {
          this.tags = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    searchClick () {
      this.getBlogList()
    },
    tagSearch (val) {
      this.ParamsData.tag_id = val
      this.getBlogList()
    }
  }
}
</script>

<style scoped>

</style>

import axios from 'axios'

export let host = 'http://127.0.0.1:8000'

export const apiMenuList = params => { return axios.get(`${host}/pages/nav/`) }

export const apiBlogList = params => { return axios.get(`${host}/blogs/blogs/`, {params: params}) }

export const apiBlogInfo = id => { return axios.get(`${host}/blogs/blogs/` + id + `/`) }

export const apiTagList = params => { return axios.get(`${host}/blogs/tags/`) }

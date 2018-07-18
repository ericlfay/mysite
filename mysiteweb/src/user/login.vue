<template>
  <div id="Login">
    <h1>klasikal Login Form</h1>
      <div class="login-form">
    <div class="close"> </div>
      <div class="head-info">
    <label class="lbl-1"> </label>
    <label class="lbl-2"> </label>
    <label class="lbl-3"> </label>
  </div>
  <div class="clear"> </div>
  <div class="avtar">
    <img src="images/avtar.png" />
  </div>
    <form>
      <input type="text" class="text" value="Username" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Username';}" >
    <div class="key">
      <input type="password" value="Password" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Password';}">
    </div>
  </form>
  <div class="signin">
    <input type="submit" value="Login" >
  </div>
</div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'Login'
}
</script>

<style>
  @import "../assets/css/style.css"
</style>

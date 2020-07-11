<template>
  <div class="layout">
    <nav id="navbar" class="sidebar sidebar-left">
      <router-link to="/" class="menu-item">
        <i class="fa fa-home mr" aria-hidden="true"></i> Home
      </router-link>
      <router-link to="/profile" class="menu-item">
        <i class="fa fa-user mr" aria-hidden="true"></i> Profile
      </router-link>
      <router-link to="/settings" class="menu-item">
        <i class="fa fa-cog mr" aria-hidden="true"></i> Settings
      </router-link>
      <router-link to="/logout" class="menu-item">
        <i class="fa fa-cog mr" aria-hidden="true"></i> Logout
      </router-link>
      <div class="user-settings menu-item">
        User <i class="fa fa-angle-down ml-auto" aria-hidden="true"></i>
      </div>
    </nav>
    <div class="feeder">
      <router-view/>
      <Feed />
    </div>
    <div id="right-sidebar" class="sidebar sidebar-right">
      <div class="search">
        <i class="fa fa-search" aria-hidden="true"></i>
        <input type="search" placeholder="Search">
      </div>
    </div>
  </div>
</template>

<script>
import Feed from './Feed.vue';

export default {
  components: {
    Feed,
  },
};
</script>

<style lang="scss" scoped>
.sidebar {
  // border: #444 1px solid;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  height: 96vh;
  padding: 15px;
}
.sidebar-left {
  width: 255px;
}
.sidebar-right {
  width: 350px;
}
.layout {
  display: grid;
  grid-template-columns: auto auto auto;
  justify-content: center;
  min-height: 100vh;
}
.feeder {
  max-width: 600px;
  width: 600px;
}
#navbar {
  display: flex;
  flex-direction: column;
}
.menu-item {
  font-size: 19px;
  font-weight: 700;
  text-decoration: none;
  color: #444;
  padding: 10px 20px 10px 15px;
  border-radius: 9999px;
  transition: 0.3s;
}
.menu-item:hover {
  color: rgb(105, 193, 248);
  background-color: rgba(135, 206, 250, 0.3);
}
.mr {
  margin-right: 15px;
}
.search {
  border: none;
  border-radius: 9999px;
  background-color: white;
  font-size: 16px;
  padding: 10px 20px;
  width: 100%;
  box-shadow: 0px 2px 2px 0px rgba(200,200,200,0.5);
}
input[type="search"] {
  border: none;
  margin-left: 15px;
  font-size: 14px;
  width: 90%;
  outline: none;
}
.user-settings {
  margin-top: auto;
}
.ml-auto {
  margin-left: auto;
}
</style>

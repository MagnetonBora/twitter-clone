<template>
  <div id="app">
    <div class="layout">
      <nav id="navbar">
        <router-link to="/">Home</router-link>
        <!-- <router-link to="/about">About</router-link> -->
      </nav>
      <div class="feeder">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #444;
  background-color: #F2F3F5;
}
.layout {
  display: grid;
  grid-template-columns: 2fr 7fr 1fr;
}
.feeder {
  display: grid;
}
div {
  // border: 1px solid lightgrey;
}
</style>

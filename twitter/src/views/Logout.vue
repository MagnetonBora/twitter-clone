<template>
  <div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$store.commit('setAuthUser', { authUser: {}, isAuthenticated: false });
    this.$store.commit('removeToken');
    this.$router.push({ name: 'Login' });
  },
};
</script>

<style lang="scss" scoped>

</style>

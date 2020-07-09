<template>
    <div class="wrapper">
      <Tweet :status="status.reply_to" :has_reply="true"/>
      <Tweet :status="status" :is_reply="true"/>
    </div>
</template>

<script>
import Tweet from './Tweet.vue';

export default {
  name: 'Reply',
  components: {
    Tweet,
  },
  props: {
    status: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.wrapper {
  background-color: white;
  border-radius: 15px;
  box-shadow: 0px 2px 2px 0px rgba(200,200,200,0.5);
  margin: 5px 0 10px 0;
  padding: 0 15px 0 0;
}
</style>

<template>
    <div>
      <Tweet :status="status.reply_to" :reply="true"/>
      <Tweet :status="status" />
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

</style>

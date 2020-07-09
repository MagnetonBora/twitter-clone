<template>
  <div>
    <div class="wrapper">
      <div class="info">
        <div class="icon">
          <i class="fa fa-retweet" aria-hidden="true"></i>
        </div>
        <div>
          {{ status.user.name }} Retweeted
        </div>
      </div>
      <div>
        <Tweet :status="status.retweeted_status" />
      </div>
    </div>
  </div>
</template>

<script>
import Tweet from './Tweet.vue';

export default {
  name: 'Retweet',
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
  display: flex;
  flex-direction: column;
}
.info {
  display: flex;
  flex-direction: row !important;
}
.icon {
  width: 50px;
  margin: 0 15px;
  text-align: right;
}
</style>

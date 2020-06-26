<template>
    <div>
      <div class="row">
        <div class="text-right" style="min-width: 50px;">
          <i class="fa fa-retweet" aria-hidden="true"></i>
        </div>
        <div class="col">
        {{ status.user.name }} Retweeted
        </div>
      </div>
      <Tweet :status="status.retweeted_status[0]" />
    </div>
</template>

<script>
import Tweet from './Tweet.vue';

const humanizeDuration = require('humanize-duration');

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
  methods: {
  },
  computed: {
    timeDiff() {
      const createdAt = new Date(this.status.created_at);
      const diff = new Date() - createdAt;
      return humanizeDuration(diff, { largest: 1 });
    },
  },
};
</script>

<style lang="scss" scoped>

</style>

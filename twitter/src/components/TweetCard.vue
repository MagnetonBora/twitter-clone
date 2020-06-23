<template>
  <div>
    {{ status.user.screen_name }}
    <div class="row">
      <div class="col-auto">
        <img :src="status.user.profile_image" width="50px" height="50px"/>
      </div>
      <div class="col">
        <div class="row border">
          <div class="col-auto mx-0 px-1 username">
            {{ status.user.name }}
          </div>
          <div v-if="status.user.verified" class="col-auto mx-0 px-1">
            ✔
          </div>
          <div class="col-auto mx-0 px-1">
            @{{ status.user.screen_name }}
          </div>
          <div class="col-auto mx-0 px-1">
            • {{ timeDiff }} ago
          </div>
        </div>
        <div class="row border">
          <div class="col mx-0 px-1">
          {{ status.text }}
          </div>
        </div>
        <div v-if="status.quoted_status" class="row border">
          <TweetCard :status="status.quoted_status[0]"/>
        </div>
        <div class="row border">
          <div class="col-auto border text-center mx-3">
            Replies
          </div>
          <div class="col-auto border text-center mx-3">
            Retweets
          </div>
          <div class="col-auto border text-center mx-3">
            ❤ {{ status.favourited.length }}
          </div>
          <div class="col-auto border text-center mx-3">
            Share
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const humanizeDuration = require('humanize-duration');

export default {
  name: 'TweetCard',
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
  mounted() {
    console.log();
  },
};
</script>

<style lang="scss" scoped>

</style>

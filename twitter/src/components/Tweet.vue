<template>
  <div>
    <div class="row">
      <div class="col-auto px-0">
        <div v-if="status.user.profile_image">
        <img :src="status.user.profile_image" class="circle-border"/>
        </div>
        <div v-else>
          <div class="circle-border initials">
            {{ userInitials }}
          </div>
        </div>
      </div>
      <div class="col">
        <div class="row">
          <div class="pl-3 username font-weight-bold">
            {{ status.user.name }}
          </div>
          <div v-if="status.user.verified">
            ✔
          </div>
          <div>
            @{{ status.user.screen_name }}
          </div>
          <div>
            • {{ timeDiff }} ago
          </div>
        </div>
        <div class="row">
          <div class="col">
          {{ status.text }}
          </div>
        </div>
        <div class="row">
          <div class="col">
            <Quote :status="status.quoted_status[0]" class="my-2" />
          </div>
        </div>
        <div class="row mt-1">
          <div class="col">
            <i class="fa fa-comment-o" aria-hidden="true"></i> {{ status.reply_count }}
          </div>
          <div class="col">
            <i class="fa fa-retweet" aria-hidden="true"></i> {{ status.retweet_count }}
          </div>
          <div class="col">
            <i class="fa fa-heart-o" aria-hidden="true"></i> {{ status.favourite_count }}
          </div>
          <div class="col">
            <i class="fa fa-share-alt" aria-hidden="true"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Quote from './Quote.vue';

const humanizeDuration = require('humanize-duration');

export default {
  name: 'Tweet',
  components: {
    Quote,
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
    userInitials() {
      return this.status.user.name.match(/\b(\w)/g).join('');
    },
  },
  mounted() {
    console.log();
  },
};
</script>

<style lang="scss" scoped>
.circle-border {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  min-width: 50px;
  min-height: 50px;
}
.initials {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 20px;
  background-color: rgb(85, 168, 250);
}
</style>

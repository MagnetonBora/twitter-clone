<template>
  <div>
    <div class="wrapper">
      <div class="action-item">
        <div class="action-button blue">
          <i class="fa fa-comment-o icon" aria-hidden="true"></i> {{ status.reply_count }}
        </div>
      </div>
      <div class="action-item">
        <div class="action-button green">
          <i class="fa fa-retweet icon" aria-hidden="true"></i> {{ status.retweet_count }}
        </div>
      </div>
      <div class="action-item">
        <div class="action-button red">
          <i class="fa fa-heart-o icon" aria-hidden="true"></i> {{ status.favourite_count }}
        </div>
      </div>
      <div class="action-item">
        <div class="action-button blue">
          <i class="fa fa-share-alt icon" aria-hidden="true"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TweetActionBar',
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
  flex-direction: row;
  // border: 1px solid lightgreen;
  padding: 1px;
}
.action-item {
  display: flex;
  width: 25%;
}
.action-button {
  display: flex;
  align-items: center;
  transition: 0.3s;
}
.icon {
  padding: 10px;
  border-radius: 15px;
  transition: 0.3s;
}
.blue:hover {
  color: rgb(105, 193, 248);
}
.blue:hover .icon {
  color: rgb(105, 193, 248);
  background-color: rgba(135, 206, 250, 0.3);
}
.green:hover {
  color: rgb(94, 219, 156);
}
.green:hover .icon {
  color: rgb(94, 219, 156);
  background-color: rgba(105, 248, 177, 0.3);
}
.red:hover {
  color: rgb(219, 94, 94);
}
.red:hover .icon {
  color: rgb(219, 94, 94);
  background-color: rgba(248, 105, 105, 0.3);
}
</style>

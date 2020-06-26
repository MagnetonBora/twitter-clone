<template>
    <div>
      <Tweet :status="status" />
      <Tweet :status="status.reply_to" />
    </div>
</template>

<script>
export default {
  name: 'Reply',
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

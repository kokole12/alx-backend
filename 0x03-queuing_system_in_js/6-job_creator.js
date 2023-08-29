import { createQueue } from "kue";

const queue = createQueue()

const notification = {
    phoneNumber: "",
    message: ""
}

const job = queue.create('push_notification_code', notification).save(function(error) {
    if (!error) {
        console.log(`Notification created with: ${job.id}`)
    }
});

job.on('complete', function() {
    console.log('Notification job completed');
}).on('failed', function() {
    console.log('Notification job failed');
});

import http from 'k6/http';
import { check } from 'k6';

export let options = {
    vus: 5, // 5 виртуальных пользователей
    duration: '10s',
};

export default function () {
    let res = http.get('http://localhost:8000/');
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response time < 500ms': (r) => r.timings.duration < 500,
    });
}
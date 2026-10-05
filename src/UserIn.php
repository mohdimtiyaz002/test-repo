<?php

class UserIn {
    public string $first_name;
    public string $last_name;
    public int $age;

    public function __construct(string $first_name, string $last_name, int $age) {
        $this->first_name = $first_name;
        $this->last_name = $last_name;
        $this->age = $age;
    }
}

class BaseResponse {
    public bool $success;

    public function __construct(bool $success) {
        $this->success = $success;
    }
}

class UserListOut {
    public array $data;

    public function __construct(array $data) {
        $this->data = $data;
    }
}
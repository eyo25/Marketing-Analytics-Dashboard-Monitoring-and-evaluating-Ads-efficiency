CREATE TABLE telegram_post_performance (
    id SERIAL PRIMARY KEY,
    post_id TEXT NOT NULL,
    date DATE NOT NULL,
    post_link TEXT,
    views INTEGER,
    post_hour TIME,
    bank TEXT,
    time_of_day TEXT
);

CREATE TABLE google_play_reviews (
    id SERIAL PRIMARY KEY,
    user_name TEXT,
    review_id TEXT NOT NULL,
    user_image TEXT NOT NULL
    at DATE NOT NULL,
    app_version INTEGER,
    score INTEGER NOT NULL,
    app_name TEXT NOT NULL
);

CREATE TABLE google_play_downloads (
    id SERIAL PRIMARY KEY,
    app_name TEXT NOT NULL,
    date DATE NOT NULL,
    daily_downloads INTEGER,
    monthly_downloads INTEGER
);

CREATE TABLE telegram_channel_growth (
    id SERIAL PRIMARY KEY,
    channel_name TEXT NOT NULL,
    date DATE NOT NULL,
    daily_subscriptions INTEGER,
    total_subscriptions INTEGER
);

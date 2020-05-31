height = 100  # meters
after_bounce_height = 0.6  # Each time ball hits the ground, it bounces back up to 3/5 the height it fell
first_ten_bounces = 10

for bounce in range(1, first_ten_bounces+1):
    print(bounce, round(height * after_bounce_height, 4))
    height *= after_bounce_height

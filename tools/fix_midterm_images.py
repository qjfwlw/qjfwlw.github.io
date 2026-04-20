from pathlib import Path

root = Path('c:/work/qjfwlw.github.io')
files = [
    root / '_posts' / '중간고사' / '2026-04-17-중간고사-사무자동화.md',
    root / '_posts' / '중간고사' / '2026-04-17-중간고사db-실습.md',
]
old_names = [
    '스크린샷 2026-04-17 121228.png',
    '스크린샷 2026-04-17 121550.png',
    '스크린샷 2026-04-17 121557.png',
    '스크린샷 2026-04-17 121657.png',
    '스크린샷 2026-04-17 121930.png',
    '스크린샷 2026-04-17 121935.png',
    '스크린샷 2026-04-17 122038-1.png',
    '스크린샷 2026-04-17 122133.png',
    '스크린샷 2026-04-17 122232.png',
    '스크린샷 2026-04-17 122304-2.png',
    '스크린샷 2026-04-17 122408-3.png',
    '스크린샷 2026-04-17 122446-3.png',
    '스크린샷 2026-04-17 122717-3.png',
    '스크린샷 2026-04-17 122837-2.png',
    '스크린샷 2026-04-17 123023-2.png',
    '스크린샷 2026-04-17 123136.png',
    '스크린샷 2026-04-17 124321.png',
    '스크린샷 2026-04-17 124449.png',
    '스크린샷 2026-04-17 124616.png',
    '스크린샷 2026-04-17 124909.png',
    '스크린샷 2026-04-17 125133.png',
    '스크린샷 2026-04-17 130114.png',
    '스크린샷 2026-04-17 130555.png',
]
image_names = ['image.png'] + [f'image-{i}.png' for i in range(1, 9)]
for path in files:
    text = path.read_text(encoding='utf-8')
    for old in old_names:
        new_name = old.replace('스크린샷 ', 'midterm-').replace(' ', '-')
        text = text.replace(f'](<{old}>)', f'](/assets/img/posts/midterm/{new_name})')
        text = text.replace(f']({old})', f'](/assets/img/posts/midterm/{new_name})')
    for old in image_names:
        text = text.replace(f']({old})', f'](/assets/img/posts/midterm/{old})')
    path.write_text(text, encoding='utf-8')
    print(f'Updated {path.name}')

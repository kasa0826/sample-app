# カメラ撮影サンプル

## 構成
- frontend/index.html
  - HTML / CSS / JavaScript を1ファイルにまとめた GitHub Pages 用フロント
- backend/app.py
  - Render 用 Flask バックエンド

## フロントの使い方
1. `frontend/index.html` を GitHub Pages に配置
2. ファイル内の `DEFAULT_API_BASE_URL` を Render のURLへ変更
   - 例: `https://camera-sample-backend.onrender.com`

## バックエンドの使い方
1. `backend` フォルダを Render にデプロイ
2. `requirements.txt` と `render.yaml` を同じ階層に置く
3. デプロイ後、発行されたURLをフロント側へ設定

## API
### POST /upload
form-data で `photo` を送信

レスポンス例:
```json
{
  "message": "撮影した写真はこちらです",
  "datetime": "2026-03-24 10:30:00",
  "image_url": "https://your-render-service.onrender.com/uploads/sample.jpg",
  "filename": "20260324_103000_abcd1234.jpg"
}
```

## 注意
- スマホでカメラを直接起動するには `input type="file"` と `capture="environment"` を利用
- GitHub Pages と Render はどちらも HTTPS なのでスマホ利用向き
- Render のローカル保存は永続ではないことがあるため、本番では Persistent Disk や外部ストレージを推奨

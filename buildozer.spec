name: Android Build
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Buildozer Action
        uses: ArtemSerebriakov/buildozer-action@v1
        with:
          buildozer_version: master
          # FIXED: This command bypasses the root warning by piping 'yes'
          command: sh -c "yes | buildozer android debug"
          repository_read_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: JosephApp-Debug
          path: bin/*.apk

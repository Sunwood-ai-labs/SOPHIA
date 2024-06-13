<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/S.O.P.H.I.A..jpg" width="100%">
<br>
<h1 align="center">S.O.P.H.I.A.</h1>
<h2 align="center">
  ～ Self-Organizing Personal Hosting Integrated Application ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/SOPHIA">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/SOPHIA">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/SOPHIA">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/SOPHIA">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/SOPHIA">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/SOPHIA">
<a href="https://github.com/Sunwood-ai-labs/SOPHIA" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=SOPHIA&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/SOPHIA">
<a href="https://github.com/Sunwood-ai-labs/SOPHIA"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/SOPHIA/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/SOPHIA"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/SOPHIA"></a>
<a href="https://github.com/Sunwood-ai-labs/SOPHIA"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/SOPHIA"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/SOPHIA?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/SOPHIA?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/SOPHIA/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 🌟 イントロダクション

S.O.P.H.I.A.は、制約のあるサーバー上のDockerの中にさらにDocker環境を構築（DinD）することで自由な開発環境を手に入れるプロジェクトです。これにより、開発者は制約に縛られることなく、柔軟で強力な開発環境を構築することができます。さらに、ローカル環境からDockerコンテナ内へのSSH接続やGPUの使用も可能です。

## 🎥 デモ

(デモ動画やGIFがあればここに挿入)

## 🚀 スタートガイド

このリポジトリは、Docker Composeを使ってS.O.P.H.I.A.を簡単に実行するための設定を提供します。S.O.P.H.I.A.をすぐに使い始めるには、以下の手順に従ってください。

**手順:**

1. **リポジトリのクローン:**

   ```bash
   git clone https://github.com/Sunwood-ai-labs/SOPHIA.git
   cd SOPHIA
   ```

2. **Docker Composeの起動:**

   ```bash
   docker-compose up -d
   ```

3. **S.O.P.H.I.A.の実行:**

   ```bash
   docker-compose exec sophia [command]
   ```

   **例:**

   ```bash
   docker-compose exec sophia bash
   ```

これにより、制約のないDocker環境内でbashシェルが起動し、自由に開発作業を行うことができます。

**SSH接続:**

ローカル環境からDockerコンテナ内へのSSH接続も可能です。以下のコマンドを使用してください。

```bash
cd secret
ssh root@localhost -p 2332 -i id_ed25519_for_SOPHIA
```

このコマンドは、`secret`ディレクトリに移動し、`id_ed25519_for_SOPHIA`秘密鍵を使用してポート2332経由でDockerコンテナ内にSSH接続します。

**GPU使用:**

S.O.P.H.I.A.はGPUの使用もサポートしています。`docker-compose.yml`ファイルの設定を調整することで、コンテナ内でGPUを利用できます。

## 📝 更新情報



## 📝 開発用

```bash
sourcesage -f docs\.sourcesage_releasenotes.yml
```

##  🤝 コントリビューション



## 📄 ライセンス



## 🙏 謝辞



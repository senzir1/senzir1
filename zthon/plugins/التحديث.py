import asyncio
import os
import sys
from git import Repo, GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_or_reply
from zthon import zedub

plugin_category = "الادوات"
cmdhd = Config.COMMAND_HAND_LER
LOGS = logging.getLogger(__name__)

UPSTREAM_REPO_URL = Config.UPSTREAM_REPO_URL or "https://github.com/senzir1/senzir1.git"
UPSTREAM_REPO_BRANCH = "main"

requirements_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "requirements.txt"
)

async def update_requirements():
    try:
        process = await asyncio.create_subprocess_shell(
            f"{sys.executable} -m pip install -r {requirements_path}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if process.returncode == 0:
            return True
        LOGS.error(stderr.decode())
        return False
    except Exception as e:
        LOGS.error(str(e))
        return False

async def restart_bot():
    os.execv(sys.executable, [sys.executable] + sys.argv)

@zedub.zed_cmd(
    pattern="تحديث$",
    command=("update", plugin_category),
    info={
        "header": "تحديث سورس ريفز على Render",
        "الاستـخـدام": ["{tr}تحديث"],
    },
)
async def render_update(event):
    event = await edit_or_reply(event, "⌛ جاري فحص التحديثات ...")
    try:
        repo = Repo()
    except (NoSuchPathError, GitCommandError, InvalidGitRepositoryError):
        return await event.edit("❌ لا يمكن الوصول للمجلد كـ Git repository")

    active_branch = repo.active_branch.name
    if active_branch != UPSTREAM_REPO_BRANCH:
        return await event.edit(f"⚠️ الفرع الحالي {active_branch} مختلف عن {UPSTREAM_REPO_BRANCH}")

    try:
        origin = repo.remote("origin")
    except Exception:
        origin = repo.create_remote("origin", UPSTREAM_REPO_URL)

    origin.fetch()
    commits = list(repo.iter_commits(f"{active_branch}..origin/{UPSTREAM_REPO_BRANCH}"))
    if not commits:
        return await event.edit("✅ البوت محدّث بالفعل لآخر إصدار")

    await event.edit("📥 جاري تحميل التحديثات ...")
    try:
        origin.pull()
    except Exception as e:
        return await event.edit(f"❌ خطأ في تحديث الكود:\n`{str(e)}`")

    await event.edit("📦 جاري تحديث المتطلبات ...")
    if not await update_requirements():
        return await event.edit("⚠️ تم التحديث لكن فشل تحديث المتطلبات!")

    await event.edit("♻️ تم التحديث بنجاح!\n🔄 جاري إعادة تشغيل البوت ...")
    await asyncio.sleep(2)
    await restart_bot()
    

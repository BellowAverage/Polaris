
--- 
title:  yolov8训练中断后重新开始训练 
tags: []
categories: [] 

---
## **需要做三件事：**

### 

### 第一件事：

 将cfg中的default.yaml配置文件中的resume参数改成True。

### 

### 第二件事：

将engine中的model.py的self.model = self.trainer.model这行代码注释掉。

```
 if not overrides.get('resume'):  # manually set model only if not resuming
            self.trainer.model = self.trainer.get_model(weights=self.model if self.ckpt else None, cfg=self.model.yaml)
            # self.model = self.trainer.model     # 中断再重启需要注释这行代码
        self.trainer.hub_session = self.session  # attach optional HUB session
        self.trainer.train()
```

### 

### 第三件事：

在engine中的trainer.py做以下修改

1. 将check_resume方法中的

```
    def check_resume(self):
        resume = r'G:\yolov8\ultralytics\yolo\v8\detect\runs\detect\train2\weights\last.pt'    # 加载中断时的last.pt
        # resume = self.args.resume    # 中断后重启换成上一行代码
        if resume:
            try:
                last = Path(
                    check_file(resume) if isinstance(resume, (str,
                                                              Path)) and Path(resume).exists() else get_latest_run())
                self.args = get_cfg(attempt_load_weights(last).args)
                self.args.model, resume = str(last), True  # reinstate
            except Exception as e:
                raise FileNotFoundError('Resume checkpoint not found. Please pass a valid checkpoint to resume from, '
                                        "i.e. 'yolo train resume model=path/to/last.pt'") from e
        self.resume = resume

    def resume_training(self, ckpt):
        ckpt = torch.load(r'G:\yolov8\ultralytics\yolo\v8\detect\runs\detect\train2\weights\last.pt')   # 训练中断再重启，需要加载这段代码，加载最后一次last.pt
        if ckpt is None:
            return
        best_fitness = 0.0
        start_epoch = ckpt['epoch'] + 1
        if ckpt['optimizer'] is not None:
            self.optimizer.load_state_dict(ckpt['optimizer'])  # optimizer
            best_fitness = ckpt['best_fitness']
        if self.ema and ckpt.get('ema'):
            self.ema.ema.load_state_dict(ckpt['ema'].float().state_dict())  # EMA
            self.ema.updates = ckpt['updates']
        if self.resume:
            assert start_epoch &gt; 0, \
                f'{self.args.model} training to {self.epochs} epochs is finished, nothing to resume.\n' \
                f"Start a new training without --resume, i.e. 'yolo task=... mode=train model={self.args.model}'"
            LOGGER.info(
                f'Resuming training from {self.args.model} from epoch {start_epoch + 1} to {self.epochs} total epochs')
        if self.epochs &lt; start_epoch:
            LOGGER.info(
                f"{self.model} has been trained for {ckpt['epoch']} epochs. Fine-tuning for {self.epochs} more epochs.")
            self.epochs += ckpt['epoch']  # finetune additional epochs
        self.best_fitness = best_fitness
        self.start_epoch = start_epoch
        if start_epoch &gt; (self.epochs - self.args.close_mosaic):
            LOGGER.info('Closing dataloader mosaic')
            if hasattr(self.train_loader.dataset, 'mosaic'):
                self.train_loader.dataset.mosaic = False
            if hasattr(self.train_loader.dataset, 'close_mosaic'):
                self.train_loader.dataset.close_mosaic(hyp=self.args)
```



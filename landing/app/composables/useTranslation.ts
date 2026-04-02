import { ref } from 'vue';

const locale = ref('en');

const dict = {
  en: {
    // Header
    n_features: 'Features',
    n_how: 'How it Works',
    n_use: 'Use Cases',
    n_signin: 'Sign In',
    n_get_started: 'Get Started',
    
    // Hero
    h_title: 'Ship AI features <br class="hidden sm:block" /> without the complexity',
    h_desc: 'The complete infrastructure to generate, manage, and scale AI functionality. One unified API, zero infrastructure management, and complete control over your data.',
    h_start: 'Start building for free',
    h_docs: 'Read the Docs',
    h_sub: 'No credit card required. Build your first app in 5 minutes.',
    
    // Features
    f_title: 'Everything you need to scale',
    f_desc: 'Core primitives perfectly balanced between ease-of-use and deep customization.',
    f_1_t: 'AI Generation',
    f_1_d: 'Instant access to state-of-the-art LLMs. Generate text, structured JSON, embeddings, and more in a single API call.',
    f_2_t: 'Basic Functions',
    f_2_d: 'Managed endpoints for standard tasks: summarization, classification, translation, and sentiment analysis out of the box.',
    f_3_t: 'Custom Domain',
    f_3_d: 'Map your own domain to our edge endpoints. Deliver AI features to your users completely white-labeled.',
    f_4_t: 'Extensibility',
    f_4_d: 'Easily plug in your own logic through webhooks, or fine-tune models directly on our infrastructure safely and securely.',
    
    // How It Works
    hw_title: 'How it works',
    hw_desc: 'Integrate AI into your application without learning prompt engineering, infrastructure scaling, or model management.',
    hw_1_t: 'Initialize SDK',
    hw_1_d: 'Install our lightweight client and initialize it with your project key. We handle the authentication safely.',
    hw_2_t: 'Call the API',
    hw_2_d: 'Instead of complex prompts, just define what you want and your data schema. We return typed responses perfectly.',
    hw_3_t: 'Deploy to Edge',
    hw_3_d: 'Everything runs on our globally distributed edge network, providing sub-second latency for your users everywhere.',
    
    // Use Cases
    uc_title: 'Built for teams that ship fast',
    uc_desc: 'Whether you\'re building a side project or a core enterprise feature, our infrastructure scales with you.',
    uc_1_badge: 'Startups',
    uc_1_t: 'Time to market',
    uc_1_d: 'Validate AI features in days, not months. Skip the pipeline setup and start returning value to beta users instantly.',
    uc_2_badge: 'Enterprises',
    uc_2_t: 'Enterprise scale',
    uc_2_d: 'SOC2 compliant infrastructure with SLA guarantees. Dedicated throughput and fine-grained access management.',
    uc_3_badge: 'Indie Hackers',
    uc_3_t: 'Pay per compute',
    uc_3_d: 'No fixed monthly costs or complex pricing tiers. Standardized pricing based purely on the compute you actually consume.',
    
    // CTA
    c_title: 'Ready to launch your AI features?',
    c_desc: 'Join hundreds of developers who have stopped managing infrastructure and started shipping product.',
    c_start: 'Get Started For Free',
    c_demo: 'Book a Demo',
    
    // Footer
    ft_desc: 'Beautifully designed infrastructure primitives for AI applications. Built for velocity and scale.',
    ft_prod: 'Product',
    ft_price: 'Pricing',
    ft_change: 'Changelog',
    ft_docs: 'Documentation',
    ft_comp: 'Company',
    ft_about: 'About',
    ft_blog: 'Blog',
    ft_care: 'Careers',
    ft_cont: 'Contact',
    ft_legal: 'Legal',
    ft_priv: 'Privacy Policy',
    ft_tos: 'Terms of Service',
    ft_cook: 'Cookie Policy',
    ft_rights: 'All rights reserved.'
  },
  ru: {
    // Header
    n_features: 'Возможности',
    n_how: 'Как это работает',
    n_use: 'Применение',
    n_signin: 'Войти',
    n_get_started: 'Начать',
    
    // Hero
    h_title: 'Создавайте ИИ-функции <br class="hidden sm:block" /> без лишней сложности',
    h_desc: 'Полная инфраструктура для создания, управления и масштабирования ИИ. Единый API, никакого управления инфраструктурой и полный контроль над вашими данными.',
    h_start: 'Начать бесплатно',
    h_docs: 'Документация',
    h_sub: 'Кредитная карта не требуется. Создайте приложение за 5 минут.',
    
    // Features
    f_title: 'Все необходимое для масштабирования',
    f_desc: 'Базовые примитивы, идеально сбалансированные между простотой и гибкостью настройки.',
    f_1_t: 'Генерация ИИ',
    f_1_d: 'Мгновенный доступ к передовым LLM. Генерируйте текст, структурированный JSON, эмбеддинги одним вызовом API.',
    f_2_t: 'Базовые функции',
    f_2_d: 'Управляемые эндпоинты для задач: суммаризация, классификация, перевод и анализ тональности из коробки.',
    f_3_t: 'Ваш домен',
    f_3_d: 'Привяжите свой домен к нашим граничным эндпоинтам. Предоставляйте ИИ-функции под вашим брендом.',
    f_4_t: 'Расширяемость',
    f_4_d: 'Легко подключайте свою логику через вебхуки или надежно дообучайте модели на нашей инфраструктуре.',
    
    // How It Works
    hw_title: 'Как это работает',
    hw_desc: 'Интегрируйте ИИ в свое приложение без промпт-инжиниринга, масштабирования серверов или управления моделями.',
    hw_1_t: 'Инициализация SDK',
    hw_1_d: 'Установите наш легковесный клиент и активируйте ключом проекта. Мы безопасно обработаем аутентификацию.',
    hw_2_t: 'Вызов API',
    hw_2_d: 'Вместо сложных промптов просто задайте схему ваших данных. Мы возвращаем идеально типизированные ответы.',
    hw_3_t: 'Глобальная сеть',
    hw_3_d: 'Все работает в нашей глобально распределенной сети (Edge), обеспечивая минимальную задержку для всех пользователей.',
    
    // Use Cases
    uc_title: 'Для команд, нацеленных на скорость',
    uc_desc: 'Независимо от того, создаете ли вы пет-проект или корпоративную систему, наша инфраструктура готова к нагрузкам.',
    uc_1_badge: 'Стартапы',
    uc_1_t: 'Быстрый запуск',
    uc_1_d: 'Проверяйте гипотезы за дни, а не месяцы. Начните мгновенно приносить пользу пользователям.',
    uc_2_badge: 'Предприятия',
    uc_2_t: 'Корпоративный масштаб',
    uc_2_d: 'Инфраструктура по стандарту SOC2 с гарантией SLA. Выделенная пропускная способность и контроль доступа.',
    uc_3_badge: 'Инди-разработчики',
    uc_3_t: 'Оплата за вычисления',
    uc_3_d: 'Стандартизированное ценообразование, основанное исключительно на тех ресурсах, которые вы фактически потребляете.',
    
    // CTA
    c_title: 'Готовы запустить свои ИИ-функции?',
    c_desc: 'Присоединяйтесь к разработчикам, которые престали управлять серверами и начали выпускать продукты.',
    c_start: 'Начать бесплатно',
    c_demo: 'Заказать демо',
    
    // Footer
    ft_desc: 'Элегантные базовые примитивы инфраструктуры для ИИ-приложений. Создано для скорости и масштаба.',
    ft_prod: 'Продукт',
    ft_price: 'Цены',
    ft_change: 'Журнал изменений',
    ft_docs: 'Документация',
    ft_comp: 'Компания',
    ft_about: 'О нас',
    ft_blog: 'Блог',
    ft_care: 'Карьера',
    ft_cont: 'Контакты',
    ft_legal: 'Юридическая информация',
    ft_priv: 'Конфиденциальность',
    ft_tos: 'Условия использования',
    ft_cook: 'Политика Cookie',
    ft_rights: 'Все права защищены.'
  }
};

export const useTranslation = () => {
  const toggleLocale = () => {
    locale.value = locale.value === 'en' ? 'ru' : 'en';
  };
  
  const setLocale = (lang: 'en' | 'ru') => {
    locale.value = lang;
  };

  const t = (key: string) => {
    return dict[locale.value as 'en' | 'ru'][key as keyof typeof dict['en']] || key;
  };

  return {
    locale,
    toggleLocale,
    setLocale,
    t
  };
};
